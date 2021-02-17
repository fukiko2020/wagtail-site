# Generated by Django 3.1.6 on 2021-02-16 12:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210216_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycolumnpage',
            name='three_column',
        ),
        migrations.RemoveField(
            model_name='mycolumnpage',
            name='two_column',
        ),
        migrations.AddField(
            model_name='mycolumnpage',
            name='body',
            field=wagtail.core.fields.StreamField([('two_column', wagtail.core.blocks.StreamBlock([('column_1_1', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())]))], group='Columns', template='home/blocks/two_column_block.html'))], label='two column', required=False)), ('three_column', wagtail.core.blocks.StreamBlock([('column_1_1_1', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())])), ('column_2', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('richtext', wagtail.core.blocks.RichTextBlock())]))], group='Columns', template='home/blocks/three_column_block.html'))], label='three column', required=False))], default=None),
            preserve_default=False,
        ),
    ]
