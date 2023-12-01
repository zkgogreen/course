# Generated by Django 4.2.4 on 2023-09-15 12:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bab', models.CharField(max_length=50)),
                ('premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perubahan', models.CharField(max_length=225)),
                ('approve', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('soal', models.CharField(max_length=224)),
                ('answer', models.CharField(max_length=224)),
                ('dummy', models.CharField(max_length=224)),
                ('penjelasan', models.TextField(default='Belum ada penjelasan')),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(max_length=224)),
                ('bahasa', models.CharField(blank=True, choices=[('EN', 'English'), ('JP', 'Japan'), ('SA', 'Arab'), ('CN', 'China')], max_length=3)),
                ('slug', models.SlugField(max_length=30, null=True)),
                ('photo', models.FileField(default='kelas/default.jpg', upload_to='kelas')),
                ('keterangan', models.CharField(blank=True, max_length=224)),
                ('defaultget', models.BooleanField(default=False)),
                ('biaya', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('premium', models.BooleanField(default=False)),
                ('mahkota', models.IntegerField(default=0)),
                ('dilihat', models.IntegerField(default=0)),
                ('certificate', models.BooleanField(default=False)),
                ('rilis', models.BooleanField(default=False)),
                ('urutan', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urutan', models.IntegerField(blank=True, null=True)),
                ('judul', models.CharField(max_length=224)),
                ('keterangan', models.CharField(default='belum ada keterangan', max_length=224)),
                ('vidio', models.URLField(blank=True, null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_mulai', models.DateField(blank=True, null=True)),
                ('tgl_berakhir', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soal', models.CharField(max_length=224)),
                ('answer', models.CharField(max_length=224)),
                ('wrong1', models.CharField(max_length=224)),
                ('wrong2', models.CharField(max_length=224)),
                ('wrong3', models.CharField(max_length=224)),
                ('penjelasan', models.TextField(default='Belum ada penjelasan')),
                ('right', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('bahasa', models.CharField(blank=True, choices=[('EN', 'English'), ('JP', 'Japan'), ('SA', 'Arab'), ('CN', 'China')], default=1, max_length=3)),
                ('kuota', models.IntegerField(default=10)),
                ('private', models.BooleanField(default=False)),
                ('time', models.TimeField(blank=True, null=True)),
                ('day', models.IntegerField(blank=True, choices=[(0, 'minggu'), (1, 'senin'), (2, 'selasa'), (3, 'rabu'), (4, 'kamis'), (5, 'jumat'), (6, 'sabtu')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.IntegerField(default=0)),
                ('api_key', models.CharField(max_length=50, null=True)),
                ('secret_key', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isMentored', models.BooleanField(default=False)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('like', models.IntegerField(default=5)),
                ('message', models.CharField(blank=True, max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now_add=True)),
                ('terlaksana', models.BooleanField(default=False)),
                ('feedback', models.CharField(blank=True, max_length=225, null=True)),
                ('performance', models.IntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('indo', models.CharField(max_length=50)),
                ('success', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VocabGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('indo', models.CharField(max_length=50)),
                ('img', models.FileField(default='media/vocabgroup/default.jpg', upload_to='media/vocabgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Withdrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField(default=0)),
                ('bank', models.CharField(max_length=30)),
                ('no_bank', models.CharField(max_length=18)),
                ('penerima', models.CharField(max_length=50)),
                ('tgl', models.DateField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
    ]