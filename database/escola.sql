CREATE EXTENSION pgcrypto;
CREATE TYPE account_type AS ENUM (
  'manager', 'student', 'teacher', 'supplier'
);
CREATE TABLE users (
  user_email varchar(250) NOT NULL, 
  user_password varchar(250) NOT NULL, 
  user_name varchar(250) NOT NULL, 
  user_type account_type NOT NULL, 
  document_id bigint NOT NULL, 
  user_address varchar(250) NOT NULL, 
  user_phone bigint NOT NULL, 
  PRIMARY KEY (user_email)
);
INSERT INTO users (
  user_email, user_password, user_name, 
  user_type, document_id, user_address, 
  user_phone
) 
VALUES 
  (
    'adrian@hotmail.com', 
    crypt(
      'teste123', 
      gen_salt('bf')
    ), 
    'Adrian', 
    'manager', 
    12345678900, 
    'Rua dos bobos, 0', 
    11912345678
  );
