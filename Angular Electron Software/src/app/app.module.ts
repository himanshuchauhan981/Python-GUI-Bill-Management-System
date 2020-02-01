import { BrowserModule } from '@angular/platform-browser'
import { NgModule } from '@angular/core'
import {MatFormFieldModule} from '@angular/material/form-field'
import {MatInputModule } from '@angular/material'
import {MatButtonModule} from '@angular/material/button';

import { AppRoutingModule } from './app-routing.module'
import { AppComponent } from './app.component'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { LoginComponent } from './login/login.component'

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
