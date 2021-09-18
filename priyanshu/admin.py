from django.contrib import admin
from .models import Contact, Home, About, Profile, Category, Resume, Skills, Portfolio


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1            # Gives extra field


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


# Resume
admin.site.register(Resume)

# Portfolio
admin.site.register(Portfolio)

# Contact Form
admin.site.register(Contact)
