from django.db import models

class SavedAnswer(models.Model):
    """
    A simple model to store a question and its answer.
    """
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display the first part of the question for convenience
        return f"Question: {self.question[:50]}..."
