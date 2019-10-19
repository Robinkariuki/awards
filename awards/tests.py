from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,bio='Test Bio',contact_info='0723030837',profile_Id=1)
        self.new_profile.save_profile()
        self.new_project = Project(id=1,title='title',details='details',link='www.link.com',user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_instance(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_profile(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

    def test_fetch_projects(self):
        self.new_project.save_project()
        projects = Project.fetch_all_images()
        self.assertTrue(len(projects)>0)

    def test_find_project(self):
        self.new_project.save_project()
        project = Project.get_single_project(self.new_project.id)
        self.assertTrue(project == self.new_project)