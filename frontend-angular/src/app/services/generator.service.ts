import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Network } from '../types/network.type';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GeneratorService {

  BaseURL:string;
  

  constructor(private http: HttpClient) {
    this.BaseURL = environment.url;
  }

  generateAddress(selectedNetwork: Network){
    return this.http.get(this.BaseURL+selectedNetwork.endpoint);
  }

}
