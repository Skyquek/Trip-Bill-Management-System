import strawberry
from typing import List
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, CategoryPartialInput, RegisterInput, BillInput, BillPartialInput, IndividualSpendingInput, IndividualSpendingPartialInput
from strawberry_django import mutations
from .. import models
from django.contrib.auth.tokens import default_token_generator

from .types import IndividualSpendingScalar, BillScalar, CategoryScalar, UserScalar, AuthResponse
from .filters import UserFilter, BillFilter, IndividualSpendingFilter, CategoryFilter

from gqlauth.user import arg_mutations as mutationsAuth
from gqlauth.user.queries import UserQueries

from strawberry.django import auth
from .types import UserAuth
from .inputs import UserLoginInput

@strawberry.type
class Query(UserQueries):
    loggedUser: UserAuth = auth.current_user()
    
    category: List[CategoryScalar] = strawberry.django.field(filters=CategoryFilter)
    
    # will need to update this, since already change to strawberry auth
    # for admin used to track how many users in the system and etc.
    users: List[UserScalar] = strawberry.django.field()
    user: List[UserScalar] = strawberry.django.field(filters=UserFilter)

    # Get bill by user id? How to do this?
    bill: List[BillScalar] = strawberry.django.field(filters=BillFilter)
    
    individualSpending: List[IndividualSpendingScalar] = strawberry.django.field(filters=IndividualSpendingFilter)
    
@strawberry.type
class Mutation:
    # User Login
    login: UserAuth = auth.login()
    logout = auth.logout()
    registerUser: UserAuth = auth.register(UserLoginInput)
    
    # create
    createCategory: CategoryScalar = mutations.create(CategoryInput)
    createBill: BillScalar = mutations.create(BillInput)
    createIndividualSpending: IndividualSpendingScalar = mutations.create(IndividualSpendingInput)
    
    # update
    updateCategory: List[CategoryScalar] = mutations.update(CategoryPartialInput, filters=CategoryFilter)
    updateBill: List[BillScalar] = mutations.update(BillPartialInput, filters=BillFilter)
    updateIndividualSpending: List[IndividualSpendingScalar] = mutations.update(IndividualSpendingPartialInput, filters=IndividualSpendingFilter)
    
    # delete
    # TODO:this is dangerous, they can feed in deletion all without filter
    deleteCategory: List[CategoryScalar] = mutations.delete(filters=CategoryFilter)
    deleteBill: List[BillScalar] = mutations.delete(filters=BillFilter)
    deleteIndividualSpending: List[IndividualSpendingScalar] = mutations.delete(filters=IndividualSpendingFilter)
    
    
    # User Authentication Mutations
    register = mutationsAuth.Register.field
    verify_token = mutationsAuth.VerifyToken.field
    update_account = mutationsAuth.UpdateAccount.field
    archive_account = mutationsAuth.ArchiveAccount.field
    delete_account = mutationsAuth.DeleteAccount.field
    password_change = mutationsAuth.PasswordChange.field
    captcha = mutationsAuth.Captcha.field
    token_auth = mutationsAuth.ObtainJSONWebToken.field
    verify_account = mutationsAuth.VerifyAccount.field
    resend_activation_email = mutationsAuth.ResendActivationEmail.field
    send_password_reset_email = mutationsAuth.SendPasswordResetEmail.field
    password_reset = mutationsAuth.PasswordReset.field
    password_set = mutationsAuth.PasswordSet.field
    refresh_token = mutationsAuth.RefreshToken.field
    revoke_token = mutationsAuth.RevokeToken.field
    
        
schema = strawberry.Schema(query=Query, mutation=Mutation)