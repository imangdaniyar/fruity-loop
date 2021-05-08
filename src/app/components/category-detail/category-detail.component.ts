import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Category } from '../../models'
import { CategoriesService } from '../../services/categories.service'


@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.css']
})
export class CategoryDetailComponent implements OnInit {
  product: Category[] = [];
  id: any;

  constructor(private route: ActivatedRoute, private categoryService: CategoriesService) { }

  ngOnInit(): void {
    this.getProduct()
  }

  getProduct(){
    this.route.paramMap.subscribe((params)=> {
      this.id = params.get('id');
      this.categoryService.getProduct(+this.id).subscribe( (data) => {
        this.product = data;
      });
    });
  }

}
