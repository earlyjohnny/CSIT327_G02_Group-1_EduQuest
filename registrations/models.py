from django.db import models


class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="registrations",
    )

    event = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name="registrations",)
    timestamp = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "registration"

    def __str__(self):
        return f"Reg #{self.reg_id} - {self.user} for {self.event}"


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="attendances",
    )

    event = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name="attendances",)
    org = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE, related_name="attendances",)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    is_excused = models.BooleanField(default=False)

    class Meta:
        db_table = "attendance"

    def __str__(self):
        return f"Attendance #{self.attendance_id} - {self.user} at {self.event}"