# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        # Add fields to MovieModel
        migrations.AddField(
            model_name='moviemodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Release Date'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='genres',
            field=models.JSONField(blank=True, default=list, verbose_name='Genres'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='director',
            field=models.CharField(blank=True, max_length=255, verbose_name='Director'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='cast',
            field=models.JSONField(blank=True, default=list, verbose_name='Cast'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='duration_minutes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duration (minutes)'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='poster_url',
            field=models.URLField(blank=True, max_length=500, verbose_name='Poster URL'),
        ),
        # Add fields to WishlistModel
        migrations.AddField(
            model_name='wishlistmodel',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='movies.customermodel', verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='movies.moviemodel', verbose_name='Movie'),
        ),
        # Add Meta options
        migrations.AlterModelOptions(
            name='moviemodel',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.AlterModelOptions(
            name='wishlistmodel',
            options={'verbose_name': 'Wishlist Item', 'verbose_name_plural': 'Wishlist Items'},
        ),
        migrations.AlterUniqueTogether(
            name='wishlistmodel',
            unique_together={('customer', 'movie')},
        ),
    ]
