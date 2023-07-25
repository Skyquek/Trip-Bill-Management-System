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
from gqlauth.core.types_ import GQLAuthError, GQLAuthErrors

from strawberry_django.permissions import (
    IsAuthenticated,
    HasPerm,
    HasRetvalPerm,
    DjangoPermissionExtension
)

from gqlauth.core.utils import get_user


class AuthRequired(DjangoPermissionExtension):
    def resolve_for_user(self, _, info, **kwargs):
        user = get_user(info)
        print(user)
        return user.is_authenticated

    has_permission = resolve_for_user

@strawberry.type
class Query(UserQueries):
    loggedUser: UserAuth = auth.current_user()

    category: List[CategoryScalar] = strawberry.django.field(
        filters=CategoryFilter)

    # will need to update this, since already change to strawberry auth
    # for admin used to track how many users in the system and etc.
    users: List[UserScalar] = strawberry.django.field()
    user: List[UserScalar] = strawberry.django.field(filters=UserFilter)
    bill: List[BillScalar] = strawberry.django.field(filters=BillFilter)
    individualSpending: List[IndividualSpendingScalar] = strawberry.django.field(filters=IndividualSpendingFilter)


@strawberry.type
class Mutation:
    # User Login
    login: UserAuth = auth.login()
    # logout = auth.logout()
    registerUser: UserAuth = auth.register(UserLoginInput)

    # create 
    createCategory: CategoryScalar = mutations.create(CategoryInput, permission_classes=[AuthRequired])
    createBill: BillScalar = mutations.create(BillInput, permission_classes=[AuthRequired])
    createIndividualSpending: IndividualSpendingScalar = mutations.create(IndividualSpendingInput, permission_classes=[AuthRequired])

    # update
    updateCategory: List[CategoryScalar] = mutations.update(CategoryPartialInput, filters=CategoryFilter, permission_classes=[AuthRequired])
    updateBill: List[BillScalar] = mutations.update(BillPartialInput, filters=BillFilter, permission_classes=[AuthRequired])
    updateIndividualSpending: List[IndividualSpendingScalar] = mutations.update(IndividualSpendingPartialInput, filters=IndividualSpendingFilter, permission_classes=[AuthRequired])

    # delete
    # TODO:this is dangerous, they can feed in deletion all without filter
    deleteCategory: List[CategoryScalar] = mutations.delete(filters=CategoryFilter, permission_classes=[AuthRequired])
    deleteBill: List[BillScalar] = mutations.delete(filters=BillFilter, permission_classes=[AuthRequired])
    deleteIndividualSpending: List[IndividualSpendingScalar] = mutations.delete(filters=IndividualSpendingFilter, permission_classes=[AuthRequired])

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
