import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  loginUser(credentials) {
    return this.http.post(`${environment.apiUrl}/login`, credentials)
  }

  get windowRef() {
    return window
  }
}
