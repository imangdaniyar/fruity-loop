import {RegistrationComponent} from './pages/registration/registration.component';
import {LoginComponent} from "./pages/login/login.component";
import {CartPageComponent} from "./pages/cart/cart-page.component";
export const appRoutes=[
    {
        path:'',
        redirectTo:'category',
        pathMatch:'full'
    },
    {
        path:'category',
        loadChildren:'./pages/category/category.module#CategoryModule'
    },
    {
        path:'product',
        loadChildren:'./pages/product/product.module#ProductModule'
    },
    {
        path:'cart',
        loadChildren:'./pages/cart/cart-page.module#CartPageModule',
        //component: CartPageComponent

    },
    {
        path : 'login',
        loadChildren : './pages/login/login.module#LoginModule',
        //component: LoginComponent
    },
    {
        path : 'registration',
        component : RegistrationComponent
    }
];
