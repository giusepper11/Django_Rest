# Generated by Django 2.1.4 on 2018-12-08 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('atracoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('enderecos', '0001_initial'),
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentario')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='enderecos.Endereco')),
            ],
        ),
    ]
