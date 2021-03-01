using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;



namespace EFGetStarted
{
    public class RestAPI
    {
        
            public bool createBlog(Blog b, String name){
                using (var db = new BloggingContext()){
                    Console.WriteLine("Inserting a new blog");
                    db.Add(new Blog { Url = "http://blogs.msdn.com/" + name });
                    db.SaveChanges();
                    }

                return true;
                
            }
            public Blog readBlog(int id, String name){
                var blog = new Blog();
                using (var db = new BloggingContext()){
                    Console.WriteLine("Querying for a blog");
                    blog = db.Blogs
                        .Find(id);    
                    }

                return blog;
                
            }
            public bool updateBlog(int id, Blog b){
                var blog = b;
                using (var db = new BloggingContext()){
                    Console.WriteLine("Updating the blog and adding a post");
                    blog.Url = "https://devblogs.microsoft.com/dotnet";
                    blog.Posts.Add( new Post { Title = "Hello World", Content = "I wrote an app using EF Core!" });
                    db.SaveChanges();    
                    }

                return true;
                
            }
            

    
    }
}