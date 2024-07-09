# Generated by Django 4.2.13 on 2024-06-29 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                (
                    'answer_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    'answer_name',
                    models.CharField(
                        max_length=255, verbose_name='Текст варианта ответа'
                    ),
                ),
                (
                    'answer_cod',
                    models.CharField(
                        max_length=50,
                        null=True,
                        verbose_name='Номер варианта ответа',
                    ),
                ),
                (
                    'f_check',
                    models.BooleanField(
                        null=True, verbose_name='Правильный ли ответ'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                (
                    'group_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    'group_name',
                    models.CharField(
                        max_length=1024,
                        verbose_name='Название группы или текст вопроса',
                    ),
                ),
                (
                    'parent_id',
                    models.IntegerField(
                        null=True, verbose_name='Группа вопросов'
                    ),
                ),
                ('app', models.CharField(max_length=255, null=True)),
                ('sort_code', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('type_id', models.IntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                (
                    'img',
                    models.ImageField(
                        null=True,
                        upload_to='images/',
                        verbose_name='Изображение',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='NameSprav',
            fields=[
                (
                    'item_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ('sprav_id', models.SmallIntegerField(default=4)),
                (
                    'item_cod',
                    models.PositiveSmallIntegerField(
                        verbose_name='Номер теста в списке тестов'
                    ),
                ),
                (
                    'item_name',
                    models.CharField(
                        max_length=255, verbose_name='Название теста'
                    ),
                ),
                (
                    'item_name_cod',
                    models.CharField(
                        max_length=255,
                        null=True,
                        verbose_name='Кол-во вопросов в тесте',
                    ),
                ),
                ('is_change', models.BooleanField(default=False, null=True)),
                ('is_active', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestPerson',
            fields=[
                (
                    'test_person_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ('person_id', models.IntegerField(null=True)),
                ('org_id', models.IntegerField()),
                ('test_config_id', models.IntegerField()),
                (
                    'dt_test',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата прохождения теста',
                    ),
                ),
                ('person_org_id', models.IntegerField()),
                (
                    'result_person',
                    models.FloatField(
                        null=True,
                        verbose_name='Результат тестирования попытка 1',
                    ),
                ),
                (
                    'amount_time',
                    models.FloatField(null=True, verbose_name='Среднее время'),
                ),
                (
                    'fio',
                    models.CharField(
                        max_length=255, verbose_name='ФИО тестируемого'
                    ),
                ),
                ('is_delete', models.BooleanField(default=False, null=True)),
                ('list_id', models.IntegerField()),
                (
                    'log_test',
                    models.CharField(
                        max_length=15,
                        null=True,
                        verbose_name='Логин для теста',
                    ),
                ),
                ('passw_test', models.CharField(max_length=15, null=True)),
                (
                    'is_passed',
                    models.PositiveSmallIntegerField(
                        default=0,
                        null=True,
                        verbose_name='Кол-во удачных прохождений теста',
                    ),
                ),
                (
                    'n_try',
                    models.PositiveSmallIntegerField(
                        null=True, verbose_name='Кол-во попыток'
                    ),
                ),
                (
                    'use_try',
                    models.PositiveSmallIntegerField(
                        null=True, verbose_name='Кол-во использованых попыток'
                    ),
                ),
                (
                    'phone',
                    models.CharField(
                        default='0',
                        max_length=63,
                        null=True,
                        verbose_name='Номер телефона',
                    ),
                ),
                (
                    'time_str',
                    models.CharField(
                        max_length=31,
                        null=True,
                        verbose_name='Время тестирования попытка 1',
                    ),
                ),
                (
                    'time_str2',
                    models.CharField(
                        max_length=31,
                        null=True,
                        verbose_name='Время тестирования попытка 2',
                    ),
                ),
                (
                    'result_person2',
                    models.FloatField(
                        null=True,
                        verbose_name='Результат тестирования попытка 2',
                    ),
                ),
                ('n_break_quest', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                (
                    'theme_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    'theme_name',
                    models.CharField(
                        max_length=255, verbose_name='Название темы'
                    ),
                ),
                (
                    'group_id',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='testing.group',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                (
                    'test_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    'section_id',
                    models.IntegerField(verbose_name='Группа вопросов'),
                ),
                ('quest_id', models.IntegerField(verbose_name='Вопрос')),
                (
                    'f_check',
                    models.BooleanField(
                        null=True, verbose_name='Правильный ли ответ'
                    ),
                ),
                (
                    'f_answer',
                    models.BooleanField(
                        default=False, verbose_name='Ответ тестируемого'
                    ),
                ),
                (
                    'n_try',
                    models.PositiveSmallIntegerField(
                        verbose_name='Номер попытки'
                    ),
                ),
                (
                    'n_q',
                    models.IntegerField(
                        null=True, verbose_name='Номер вопроса в тесте'
                    ),
                ),
                (
                    'answer_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='testing.answer',
                    ),
                ),
                (
                    'test_person_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='testing.testperson',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='theme_id',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='testing.theme',
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='quest_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='answers',
                to='testing.group',
                verbose_name='Вопрос',
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='section_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='answer_groups',
                to='testing.group',
                verbose_name='Группа вопросов',
            ),
        ),
    ]
