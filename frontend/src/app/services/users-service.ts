import { User, UserCreate } from '../model/user.model';
import Http from './http'

export const create = (user: UserCreate) => {
    return Http.post<User>('/user', user);
};

export const listUsers = (skip = 0) => {
  return Http.get<User[]>('/user' + `?skip=${skip}`);
};

export const getUserByEmail = (email: string) => {
    return Http.get<User>(`/user/${email}`);
}