import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InitialFrontComponent } from './initial-front.component';

describe('InitialFrontComponent', () => {
  let component: InitialFrontComponent;
  let fixture: ComponentFixture<InitialFrontComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InitialFrontComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InitialFrontComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
