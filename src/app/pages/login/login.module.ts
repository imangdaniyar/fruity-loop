import {NgModule} from "@angular/core";
import {RouterModule} from "@angular/router";
import {loginRoutes} from "./login.routes";
import {SharedModule} from "../../shared/shared.module";
import {LoginComponent} from "./login.component";
@NgModule({
  imports: [
    SharedModule,
    RouterModule.forChild(loginRoutes)
  ],
  declarations: [
  	LoginComponent
  ]
})
export class LoginModule { }
