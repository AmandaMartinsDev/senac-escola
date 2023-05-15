import { User, UserCreate } from '../model/user.model';
import Http from './http'

export const createUser = (user: UserCreate) => {
    return Http.post<User>('/users', user);
};

export const listUsers = (skip = 0) => {
  return Http.get<User[]>(`/users?skip=${skip}`);
};

export const getUserByEmail = (email: string) => {
    return Http.get<User>(`/users/${email}`);
}