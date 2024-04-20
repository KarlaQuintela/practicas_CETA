# Generated by Django 5.0.3 on 2024-04-20 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_cg', models.AutoField(primary_key=True, serialize=False)),
                ('name_cg', models.CharField(max_length=15, unique=True)),
                ('hourly_wage_cg', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('name_client', models.CharField(max_length=255)),
                ('address_client', models.CharField(max_length=255)),
                ('phone_client', models.CharField(max_length=50)),
                ('email_client', models.EmailField(max_length=254, verbose_name='Email')),
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
            name='Employee',
            fields=[
                ('id_em', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name_em', models.CharField(max_length=50, unique=True)),
                ('address_em', models.CharField(max_length=255)),
                ('phone_em', models.CharField(max_length=15)),
                ('email_em', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('department_em', models.CharField(max_length=255)),
                ('num_account_em', models.CharField(max_length=16, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fk_id_cg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.category')),
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
                ('manager_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.employee')),
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
            name='PaymentEmployee',
            fields=[
                ('id_pay', models.AutoField(primary_key=True, serialize=False)),
                ('hours_pay', models.IntegerField()),
                ('task', models.TextField()),
                ('amount_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fk_id_em', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.employee')),
                ('fk_id_payterm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceta.paymentterm')),
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
                ('duration_serv', models.IntegerField()),
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
