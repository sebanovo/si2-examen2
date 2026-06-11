import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';

import {
  DatabaseHealthResponse,
  HealthService,
} from './health.service';

@Component({
  selector: 'app-health-check',
  standalone: true,
  imports: [CommonModule],
  templateUrl: "./health-check.component.html",
})
export class HealthCheckComponent {
  private readonly healthService = inject(HealthService);

  readonly loading = signal(false);
  readonly response = signal<DatabaseHealthResponse | null>(null);
  readonly error = signal<string | null>(null);

  handleCheckDatabase(): void {
    this.loading.set(true);
    this.response.set(null);
    this.error.set(null);

    this.healthService.checkDatabase().subscribe({
      next: (result) => {
        this.response.set(result);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err?.message ?? 'Request failed.');
        this.loading.set(false);
      },
    });
  }
}

