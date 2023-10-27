
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_auto_20231026_0057'),
        ('reviews', '0002_review_delete_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='score',
            new_name='star',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
