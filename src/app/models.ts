

export interface Category {
  id: number;
  name: string;
  description: string;
  category: string;
  price: number;
  code: string;
  quantity: number;
  rating: number;
  photo: string;
}


export interface User {
  id: number;
  name: string;
  surname: string;
  password: string;
  email: string;
  address: string;
};

export interface TokenInfo {
  email: string;
  exp: number;
  user_id: number;
  username: string;
}

export interface AuthToken {
  token: string;
}
