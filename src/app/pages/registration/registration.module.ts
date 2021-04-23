import {NgModule} from "@angular/core";
import {RouterModule} from "@angular/router";
import {registrationRoutes} from "./registration.routes";
import {SharedModule} from "../../shared/shared.module";
import {RegistrationComponent} from "./registration.component";
@NgModule({
  imports: [
    SharedModule,
    RouterModule.forChild(registrationRoutes)
  ],
  declarations: [
  	RegistrationComponent
  ]
})
export class RegistrationModule { }
