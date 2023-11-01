from django.db import models


def image_path(instance, filename):
    return f"shop/{instance}/{filename}"


def image_detail_path(instance, filename):
    return f"shop-detail/{instance}/{filename}"


class Color(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Rating(models.Model):
    integer = models.IntegerField()


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class ImageShopDetail(models.Model):
    title = models.CharField(max_length=221)
    image1 = models.ImageField(upload_to=image_detail_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=image_detail_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=image_detail_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=image_detail_path, null=True, blank=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to=image_path)
    image_detail = models.ForeignKey(ImageShopDetail, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    is_sale = models.FloatField(null=True, blank=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
