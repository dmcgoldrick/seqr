# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-24 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def _get_variant_notes(apps, schema_editor):
    VariantNote = apps.get_model("seqr", "VariantNote")
    db_alias = schema_editor.connection.alias
    variant_notes = VariantNote.objects.using(db_alias).all()
    return variant_notes


def variant_note_to_multi_saved_variants():
    variant_notes = _get_variant_notes()
    for variant_note in variant_notes:
        variant_note.saved_variants = [variant_note.saved_variant]


def variant_note_to_single_saved_variant():
    variant_notes = _get_variant_notes()
    for variant_note in variant_notes:
        variant_note.saved_variant = variant_note.saved_variants[0]


def _get_variant_tags(apps, schema_editor):
    VariantTag = apps.get_model("seqr", "VariantTag")
    db_alias = schema_editor.connection.alias
    variant_tags = VariantTag.objects.using(db_alias).all()
    return variant_tags


def variant_tag_to_multi_saved_variants():
    variant_tags = _get_variant_tags()
    for variant_tag in variant_tags:
        variant_tag.saved_variants = [variant_tag.saved_variant]


def variant_tag_to_single_saved_variant():
    variant_tags = _get_variant_tags()
    for variant_tag in variant_tags:
        variant_tag.saved_variant = variant_tag.saved_variants[0]


def _get_functional_data(apps, schema_editor):
    VariantFunctionalData = apps.get_model("seqr", "VariantFunctionalData")
    db_alias = schema_editor.connection.alias
    functional_data = VariantFunctionalData.objects.using(db_alias).all()
    return functional_data

def variant_functional_data_to_multi_saved_variants():
    all_functional_data = _get_functional_data()
    for functional_data in all_functional_data:
        functional_data.saved_variants = [functional_data.saved_variant]


def variant_functional_data_to_single_saved_variant():
    all_functional_data = _get_functional_data()
    for functional_data in all_functional_data:
        functional_data.saved_variant = functional_data.saved_variants[0]


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seqr', '0065_merge_20190924_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(db_index=True, max_length=30, unique=True)),
                ('created_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('last_modified_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        # migrations.AddField(
        #     model_name='variantnote',
        #     name='saved_variants',
        #     field=models.ManyToManyField(to='seqr.SavedVariant'),
        # ),
        # migrations.RunPython(variant_note_to_multi_saved_variants, reverse_code=variant_note_to_single_saved_variant),
        # migrations.AddField(
        #     model_name='variantfunctionaldata',
        #     name='saved_variants',
        #     field=models.ManyToManyField(to='seqr.SavedVariant'),
        # ),
        # migrations.RunPython(variant_functional_data_to_multi_saved_variants,
        #                      reverse_code=variant_functional_data_to_single_saved_variant),
        # migrations.AddField(
        #     model_name='varianttag',
        #     name='saved_variants',
        #     field=models.ManyToManyField(to='seqr.SavedVariant'),
        # ),
        # migrations.RunPython(variant_tag_to_multi_saved_variants, reverse_code=variant_tag_to_single_saved_variant),
        # migrations.AlterUniqueTogether(
        #     name='variantfunctionaldata',
        #     unique_together=set([]),
        # ),
        # migrations.AlterUniqueTogether(
        #     name='varianttag',
        #     unique_together=set([]),
        # ),
        # migrations.RemoveField(
        #     model_name='variantnote',
        #     name='saved_variant',
        # ),
        # migrations.RemoveField(
        #     model_name='variantfunctionaldata',
        #     name='saved_variant',
        # ),
        # migrations.RemoveField(
        #     model_name='varianttag',
        #     name='saved_variant',
        # ),
    ]
