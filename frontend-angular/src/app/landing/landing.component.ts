import { Component, OnInit } from '@angular/core';
import { Network } from '../types/network.type';
import { Networks } from '../models/networks.models';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements OnInit {

  networks: Network[];
  selectedNetwork: Network | undefined;
  generator: boolean;

  constructor() {
    this.networks = Networks;
    this.generator = false;
   }

  ngOnInit(): void {}

  requestWalletAddress(){
    this.generator = true;
  }

  dialogClosed() {
    this.generator = false;
  }

}
