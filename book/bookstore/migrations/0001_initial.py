# Generated by Django 4.1.2 on 2023-07-17 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TacGia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tenTacGia', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sach',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tenSach', models.CharField(db_index=True, max_length=250)),
                ('gia', models.IntegerField()),
                ('tacGia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookstore.tacgia')),
            ],
        ),
    ]
