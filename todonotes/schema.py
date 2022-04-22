import graphene
from graphene import ObjectType
from graphene_django import  DjangoObjectType
from users.models import User
from todo.models import Todo, Project


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TodoType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return  Todo.objects.all()


schema = graphene.Schema(query=Query)

# GraphQL запрос для получения Todo, проектов и пользователей,связанных с проектом:

"""{
  allTodos {
    text
    project {
      name
      users {
        username
      }
    }
  }
}"""