import { UserType } from './user-type.enum';

export interface UserCreate {
    user_email: string;
    user_password: string;
}

export interface User {
    user_name: string;
    user_type: UserType;
    document_id: string;
    user_address: string;
    user_phone: number;
    user_email: string;
}