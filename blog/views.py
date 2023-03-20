from django.shortcuts import render
from .models import Blog
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse
from .forms import commentform
def index(request):
     allblogs=Blog.objects.all()
     allblogs.order_by('-date')
     latestblogs=allblogs[:3]
     return render(request,'blog/index.html',{
          'blogs':latestblogs
     })        

class all_blogs(ListView):
     model=Blog
     template_name='blog/all_blogs.html'
     context_object_name='blogs'
    
    #  def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     reurl=[]
    #     for ob in object:
    #        redirect_url=reverse('blog_detail',args=[object.slug])
    #        reurl.append(redirect_url)
    #     context['url']=reurl   
    #     return context

# class blog_detail(DetailView):
#      template_name='blog/blog_detail.html'
#      model=Blog
#      def get_context_data(self, **kwargs):
#          context= super().get_context_data(**kwargs)
#          tags=self.object.tags.all()
#          context['tags']=tags
#          return context
     

class blog_detail(View):
     def get(self,request,slug):
        blog=Blog.objects.get(slug=slug)
        tags=blog.tags.all()
        comment_form=commentform()        
        all_comments=blog.comments.all()
        return render(request,'blog/blog_detail.html',{'form':comment_form,'blog':blog,'all_comments':all_comments,'tags':tags})
     def post(self,request,slug):
         comment_form=commentform(request.POST)
         if comment_form.is_valid:
             cf=comment_form.save(commit=False)
             blog=Blog.objects.get(slug=slug)
             cf.post=blog
             cf.save()
             return HttpResponseRedirect(reverse('blog_detail',args=[slug]))
         else:
             blog=Blog.objects.get(slug=slug)
             all_comments=blog.comments.objects.all()
             return render(request,'blog/blog_detail.html',{'form':commentform,'blog':blog,'all_comments':all_comments})
         
class ReadLater(View):
    def get(self,request):
        stored_post=request.session.get('stored_post')
        context={}
        if stored_post is None:
            context["blogs"]=[]
            context["has_posts"]=False
        else:
            blogs=Blog.objects.filter(id__in=stored_post)
            context['blogs']=blogs
            context['has_posts']=True
          
        return render(request,'blog/readlater.html',context) 

    def post(self,request):
        stored_post=request.session.get('stored_post')
        post_id=(int)(request.POST['post_id'])

        if stored_post is  None:
            stored_post=[]
            
        if post_id not in stored_post:
            print("stored")
            stored_post.append(post_id) 
        else: 
            stored_post.remove(post_id)   
        request.session['stored_post']=stored_post     
        
        return HttpResponseRedirect('/')
                  
