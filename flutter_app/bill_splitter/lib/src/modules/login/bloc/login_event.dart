// there are three events:
// LoginUsernameChange: notifies the bloc that the username had been modified
// LoginPasswordChanged: notifies the bloc that the password has been modified
// LoginSubmitted: notifies the bloc that the form has been submitted

part of 'login_bloc.dart';

sealed class LoginEvent extends Equatable {
  const LoginEvent();

  @override
  List<Object> get props => [];
}

final class LoginUsernameChanged extends LoginEvent {
  final String username;
  const LoginUsernameChanged(this.username);

  @override
  List<Object> get props => [username];
}

final class LoginPasswordChanged extends LoginEvent {
  final String password;

  const LoginPasswordChanged(this.password);

  @override
  List<Object> get props => [password];
}

final class LoginSubmitted extends LoginEvent {
  const LoginSubmitted();
}
