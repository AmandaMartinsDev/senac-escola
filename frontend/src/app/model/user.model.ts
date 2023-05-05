export interface UserCreate {
    user_email: string;
    user_password: string;
}

export interface User {
    user_name: string;
    user_type: string;
    document_id: number;
    user_address: string;
    user_phone: number;
}