# Generated by Django 5.0.2 on 2024-03-05 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceta', '0002_alter_category_id_cg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('name_client', models.CharField(max_length=255)),
                ('address_client', models.CharField(max_length=255)),
                ('phone_client', models.CharField(max_length=50)),
                ('email_client', models.CharField(max_length=50)),
                ('description_client', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('name_role', models.CharField(max_length=255)),
                ('description_role', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id_ct', models.AutoField(primary_key=True, serialize=False)),
                ('num_ct', models.CharField(max_length=255, unique=True)),
                ('title_ct', models.CharField(max_length=255)),
                ('start_ct', models.DateField()),
                ('end_ct', models.DateField()),
                ('resolution_ct', models.DateField()),
                ('description_ct', models.TextField()),
                ('staff_count', models.IntegerField()),
                ('type_ct', models.CharField(max_length=50)),
                ('uni_area_ct', models.CharField(max_length=50)),
                ('work_area_ct', models.CharField(max_length=50)),
                ('value_ct', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_margin', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency_ct', models.CharField(max_length=10)),
                ('proposed_by', models.CharField(max_length=50)),
                ('approved_by', models.CharField(max_length=50)),
                ('is_current', models.BooleanField(default=True)),
                ('fk_id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.client')),
                ('manager_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.worker')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTerm',
            fields=[
                ('id_payterm', models.AutoField(primary_key=True, serialize=False)),
                ('due_month_payterm', models.IntegerField()),
                ('due_year_payterm', models.IntegerField()),
                ('deliver', models.CharField(max_length=50)),
                ('is_billable', models.BooleanField(default=False)),
                ('fk_id_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id_expense', models.AutoField(primary_key=True, serialize=False)),
                ('description_expense', models.CharField(max_length=255)),
                ('amount_expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fk_id_payterm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.paymentterm')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id_bill', models.AutoField(primary_key=True, serialize=False)),
                ('month_bill', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('fk_id_payterm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.paymentterm')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentWorker',
            fields=[
                ('id_payworker', models.AutoField(primary_key=True, serialize=False)),
                ('hours_payworker', models.IntegerField()),
                ('percent_payworker', models.DecimalField(decimal_places=2, max_digits=10)),
                ('task_worker', models.TextField()),
                ('amount_payworker', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fk_id_payterm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.paymentterm')),
                ('fk_id_w', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id_rec', models.AutoField(primary_key=True, serialize=False)),
                ('amoun_rec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date_rec', models.DateField()),
                ('fk_id_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.bill')),
            ],
        ),
        migrations.CreateModel(
            name='Remuneration',
            fields=[
                ('id_rem', models.AutoField(primary_key=True, serialize=False)),
                ('amount_rem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date_rem', models.DateField()),
                ('fk_id_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.bill')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_serv', models.AutoField(primary_key=True, serialize=False)),
                ('product_serv', models.CharField(max_length=255)),
                ('manager_serv', models.IntegerField()),
                ('duration_serv', models.IntegerField()),
                ('workers_count', models.IntegerField()),
                ('description_serv', models.CharField(max_length=255)),
                ('fk_id_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id_tr', models.AutoField(primary_key=True, serialize=False)),
                ('training_tr', models.CharField(max_length=255)),
                ('hours_tr', models.IntegerField()),
                ('capacity_tr', models.IntegerField()),
                ('price_tr', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_tr', models.DateField()),
                ('end_tr', models.DateField()),
                ('fk_id_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.contract')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=255)),
                ('password_user', models.CharField(max_length=255)),
                ('fk_id_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.role')),
            ],
        ),
        migrations.CreateModel(
            name='Ceta',
            fields=[
                ('id_ceta', models.AutoField(primary_key=True, serialize=False)),
                ('contrats_list', models.ManyToManyField(to='ceta.contract')),
                ('users_list', models.ManyToManyField(to='ceta.user')),
            ],
        ),
    ]