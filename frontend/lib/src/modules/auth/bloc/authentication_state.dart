part of 'authentication_bloc.dart';

class AuthenticationState extends Equatable {
  final AuthenticationStatus status;
  final User user;

  // Private named constructor
  const AuthenticationState._({
    this.status = AuthenticationStatus.unknown,
    this.user = User.empty,
  });

  // Public constructor that called the private constructor to set value
  const AuthenticationState.unknown() : this._();

  // Public constructor that called the private constructor to set value
  const AuthenticationState.authenticated(User user)
      : this._(status: AuthenticationStatus.authenticated);

  // Public constructor that called the private constructor to set value
  const AuthenticationState.unauthenticated()
      : this._(status: AuthenticationStatus.unauthenticated);

  @override
  List<Object?> get props => [status, user];
}
