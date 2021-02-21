import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-pagenotfound',
  templateUrl: './pagenotfound.component.html',
  styleUrls: ['./pagenotfound.component.scss']
})
export class PagenotfoundComponent implements OnInit {
  
  title = '404-Azkaban';

  constructor(private titleService:Title) { }

  ngOnInit(): void {
    this.titleService.setTitle(this.title);
  }
  
}
