import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesComponent } from './components/categories/categories.component';
import { AboutComponent } from './components/about/about.component';
import { UserComponent } from './components/user/user.component';
import { SettingsComponent } from './components/settings/settings.component';
import { CategoryDetailComponent } from './components/category-detail/category-detail.component';

const routes: Routes = [
  {path: 'products', component: CategoriesComponent},
  {path: 'products/:id', component: CategoryDetailComponent},
  {path: 'about', component: AboutComponent},
  {path: ':id', component: UserComponent, children: [
    {path: 'settings', component: SettingsComponent }
  ]},
  {path: '', redirectTo: 'products', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }