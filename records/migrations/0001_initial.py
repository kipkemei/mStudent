# Generated by Django 2.1.2 on 2019-04-11 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.CharField(blank=True, max_length=50)),
                ('file', models.ImageField(blank=True, null=True, upload_to='certificates')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.PositiveIntegerField(blank=True, null=True)),
                ('english', models.PositiveIntegerField(blank=True, null=True)),
                ('kiswahili', models.PositiveIntegerField(blank=True, null=True)),
                ('science', models.PositiveIntegerField(blank=True, null=True)),
                ('sst', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.PositiveIntegerField(blank=True, null=True)),
                ('english', models.PositiveIntegerField(blank=True, null=True)),
                ('kiswahili', models.PositiveIntegerField(blank=True, null=True)),
                ('chem', models.PositiveIntegerField(blank=True, null=True)),
                ('phy', models.PositiveIntegerField(blank=True, null=True)),
                ('bio', models.PositiveIntegerField(blank=True, null=True)),
                ('comp', models.PositiveIntegerField(blank=True, null=True)),
                ('bst', models.PositiveIntegerField(blank=True, null=True)),
                ('agr', models.PositiveIntegerField(blank=True, null=True)),
                ('art', models.PositiveIntegerField(blank=True, null=True)),
                ('cre', models.PositiveIntegerField(blank=True, null=True)),
                ('music', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('adm_no', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.School')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('reg_no', models.CharField(blank=True, max_length=100)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.School')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(blank=True, max_length=20, null=True)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('marks', models.PositiveIntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Student')),
            ],
        ),
        migrations.AddField(
            model_name='secondaryexam',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Student'),
        ),
        migrations.AddField(
            model_name='primaryexam',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Student'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Student'),
        ),
    ]
