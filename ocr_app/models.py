from django.db import models

class Visitor(models.Model):
    """
    Stores visitor information, including name, birth date, age, and email.
    """
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    """
    Stores document upload information, including document type, and associated visitor.
    """
    DOCUMENT_TYPE_CHOICES = [
        ('AADHAR', 'Aadhar Card'),
        ('PAN', 'Pan Card'),
    ]

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image_path = models.ImageField(upload_to='uploaded_documents/')

    def __str__(self):
        return f"{self.document_type} for {self.visitor.name}"

class VisitorPass(models.Model):
    """
    Stores visitor pass information including expiry and QR code data.
    """
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE, related_name='visitor_pass')
    qr_code_data = models.TextField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        """
        Check if the pass is expired.
        """
        return self.expiry_date < timezone.now().date()

    def __str__(self):
        return f"Pass for {self.visitor.name} - {'Expired' if self.is_expired() else 'Active'}"
