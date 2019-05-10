import graphene
import company.schema


class Query(company.schema.Query, graphene.ObjectType):
    pass


class Mutation(company.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
