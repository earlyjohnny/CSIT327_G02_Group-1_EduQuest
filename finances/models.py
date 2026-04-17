from django.db import models

class BudgetRequest(models.Model):
	req_id = models.AutoField(primary_key=True)
	org_id = models.ForeignKey(
		"organizations.Organization",
		on_delete=models.CASCADE,
		related_name="budget_requests",
		db_column="org_id",
	)
	doc_id = models.IntegerField()
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	purpose = models.TextField()
	status = models.CharField(max_length=50)
	request_date = models.DateField()

	class Meta:
		db_table = "budget_request"

	def __str__(self):
		return f"Budget Request #{self.req_id}"


class Equipment(models.Model):
	item_id = models.AutoField(primary_key=True)
	org_id = models.ForeignKey(
		"organizations.Organization",
		on_delete=models.CASCADE,
		related_name="equipment_items",
		db_column="org_id",
	)
	item_name = models.CharField(max_length=255)
	serial_number = models.CharField(max_length=100)
	condition = models.CharField(max_length=50)

	class Meta:
		db_table = "equipment"

	def __str__(self):
		return self.item_name


class EventEquipment(models.Model):
	event_equip_id = models.AutoField(primary_key=True)
	event_id = models.ForeignKey(
		"events.Event",
		on_delete=models.CASCADE,
		related_name="event_equipments",
		db_column="event_id",
	)
	item_id = models.ForeignKey(
		Equipment,
		on_delete=models.CASCADE,
		related_name="event_equipments",
		db_column="item_id",
	)
	quantity = models.IntegerField()
	assigned_date = models.DateTimeField()
	return_date = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = "event_equipment"

	def __str__(self):
		return f"Event Equipment #{self.event_equip_id}"
