# Generated by Django 3.1.6 on 2021-02-16 12:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0008_mycolumnpage_threecolumnpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycolumnpage',
            name='three_column',
            field=wagtail.core.fields.StreamField([('column_1_1_1', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_2', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())]))], group='Columns', template='home/blocks/three_column_block.html'))]),
        ),
        migrations.AlterField(
            model_name='threecolumnpage',
            name='content',
            field=wagtail.core.fields.StreamField([('column_1_1_1', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_2', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())]))], group='Columns', template='home/blocks/three_column_block.html'))]),
        ),
        migrations.DeleteModel(
            name='SidebarPage',
        ),
    ]
