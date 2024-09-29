from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def archive(request):
    return render(request, 'archive.html')

def author(request):
    return render(request, 'author.html')

def blog_list(request):
    return render(request, 'blog-list.html')

def contact(request):
    return render(request, 'contact.html')

def home_creative_blog(request):
    return render(request, 'home-creative-blog.html')

def home_creative_blog_dark(request):
    return render(request, 'home-creative-blog-dark.html')

def home_default_dark(request):
    return render(request, 'home-default-dark.html')

def home_lifestyle_blog(request):
    return render(request, 'home-lifestyle-blog.html')

def home_lifestyle_blog_dark(request):
    return render(request, 'home-lifestyle-blog-dark.html')

def home_seo(request):
    return render(request, 'home-seo.html')

def home_seo_blog(request):
    return render(request, 'home-seo-blog.html')

def home_seo_blog_dark(request):
    return render(request, 'home-seo-blog-dark.html')

def home_tech_blog(request):
    return render(request, 'home-tech-blog.html')

def home_tech_blog_dark(request):
    return render(request, 'home-tech-blog-dark.html')

def index_dark(request):
    return render(request, 'index-dark.html')

def maintenance(request):
    return render(request, 'maintenance.html')

def post_details(request):
    return render(request, 'post-details.html')

def post_format_gallery(request):
    return render(request, 'post-format-gallery.html')

def post_format_standard(request):
    return render(request, 'post-format-standard.html')

def post_format_text(request):
    return render(request, 'post-format-text.html')

def post_format_video(request):
    return render(request, 'post-format-video.html')

def post_layout_1(request):
    return render(request, 'post-layout-1.html')

def post_layout_2(request):
    return render(request, 'post-layout-2.html')

def post_layout_3(request):
    return render(request, 'post-layout-3.html')

def post_layout_4(request):
    return render(request, 'post-layout-4.html')

def post_layout_5(request):
    return render(request, 'post-layout-5.html')

def post_list(request):
    return render(request, 'post-list.html')

def practice(request):
    return render(request, 'practice.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def typography(request):
    return render(request, 'typography.html')
