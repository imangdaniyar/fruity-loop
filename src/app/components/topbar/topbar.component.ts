import { Component, OnInit } from '@angular/core';
import {CartService} from "../../services/cart.service";

@Component({
    selector: 'top-bar',
    styleUrls: ['./top-bar.component.css'],
    template: `    
    <div class="main-header navbar-fixed-top">
        <div class="header-menu">
            <div class="header-nav-wrapper">
                <ul class="header-nav" style = "float:left">
                    <li class="header-nav-item">
                        <a routerLink="/">STORE</a>
                    </li>
                    <li class="header-nav-item">
                        <a routerLink="/">ABOUT</a>
                    </li>
                </ul>
                <p style = "text-align:center"> LOGO </p>
            </div>
            <div class="header-cart-wrapper">
                <ul class="header-nav" style="float:right">
                    <li class="header-nav-item">
                        <a routerLink="/login">LOGIN</a>
                    </li>
                    <li class="header-nav-item">
                        <a routerLink="/registration">REGISTRATION</a>
                    </li>
                </ul>
                <div class="header-cart" (click)="toggleCartPopup($event)" style = "float:right">
                    <div class="mobil-shopping-cart">
                        <span><i class="fa fa-shopping-cart fa-2x"></i> <span *ngIf="cart_num">( {{cart_num}} )</span></span>
                    </div>
                    <div class="header-cart-item">
                        <a href="">MY CART <span *ngIf="cart_num">( {{cart_num}} )</span><span class="fa fa-caret-down"></span></a>
                    </div>
                </div>
            </div>
        </div>
        <cart-popup></cart-popup>
    </div>
`
})
export class TopbarComponent implements OnInit {
    public collapse: boolean = false;
    public cart_num:number;
    constructor(
        private cartService: CartService
    ) { }

    ngOnInit() {
        this.cartService.cartListSubject
            .subscribe(res => {
                this.cart_num = res.length;
            })
    }
    toggleCartPopup = (event) => {
        event.preventDefault();
        event.stopPropagation();
        this.cartService.toggleCart()
    }
}