import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { GeneratorResponse, Keys, Network } from '../types/network.type';
import { GeneratorService } from '../services/generator.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-generator',
  templateUrl: './generator.component.html',
  styleUrls: ['./generator.component.css']
})
export class GeneratorComponent implements OnInit, OnChanges {
  @Input() selectedNetwork: Network | undefined; 
  @Input() inView: boolean = false;

  status: string = '';
  loading: boolean;
  keys: Keys;
  showDownload: boolean = false;
  link: string = "";

  constructor(private generatorService:GeneratorService) {
    this.loading = true;
    this.keys = {privkey:'',pubkey:''};

   }

  ngOnInit(): void {}

  ngOnChanges(): void {
    if (this.selectedNetwork != undefined && this.inView){
      this.status = `Generating ${this.selectedNetwork?.symbol} address`;
      this.callEndpoint();
    }
  }

  callEndpoint(){
    if (this.selectedNetwork == undefined) {
      this.status = "Please close the pop up and reselect the network";
    }
    else {
      this.generatorService.generateAddress(this.selectedNetwork).subscribe((data: any) => {
        this.status = data.result
        this.loading = false;
        if (data.result == "ok"){
          this.status = "Copy the details below and store it a safe place!"
          this.keys.pubkey = data.data.pubkey;
          this.keys.privkey = data.data.privkey;
          this.showDownload = true;
          this.link = `${environment.url}/download/${data.download}`
        }
      })
    }

  }

}
