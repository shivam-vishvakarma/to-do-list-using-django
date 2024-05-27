from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100,null=False)
    count = models.PositiveIntegerField(default=1, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new instance being created
            last_instance = self.__class__.objects.order_by('-count').first()
            if last_instance:
                self.count = last_instance.count + 1
        super(Task, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # If an instance is deleted, decrement the count for subsequent instances
        self.count -= 1
        self.save()
        super(Task, self).delete(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk}, Count: {self.count}"