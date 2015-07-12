from django.contrib import admin

from .models import CommunityRole, Sector, TypeSocialNetwork, SocialNetwork
from .models import Community
# Register your models here.
admin.site.register(CommunityRole)
admin.site.register(Sector)
admin.site.register(TypeSocialNetwork)
admin.site.register(SocialNetwork)
admin.site.register(Community)