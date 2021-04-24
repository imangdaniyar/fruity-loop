import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {User} from "../../model/user";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  username:string;
  email:string;
  password:string;
  users: User[] = [];
  constructor( private router: Router ) { }
  addUser(){
    console.log(this.username,this.password,this.email);
    this.users.push(new User(this.username,this.password,this.email));
  }
  ngOnInit() {
  }

}
