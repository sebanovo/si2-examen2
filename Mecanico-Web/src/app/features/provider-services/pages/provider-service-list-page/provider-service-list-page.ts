import { Component, inject, OnDestroy, OnInit, signal } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideArrowLeft,
	lucideInbox,
	lucideWrench,
} from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { ProviderServiceTable } from "../../components/provider-service-table/provider-service-table";
import { ProviderServicesStore } from "../../store/provider-service.store";

@Component({
	selector: "app-provider-service-list-page",
	imports: [
		NgIcon,
		HlmButtonImports,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		ProviderServiceTable,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideArrowLeft,
			lucideInbox,
			lucideWrench,
		}),
	],
	templateUrl: "./provider-service-list-page.html",
	styleUrl: "./provider-service-list-page.css",
})
export class ProviderServiceListPage implements OnInit, OnDestroy {
	readonly store = inject(ProviderServicesStore);
	private readonly route = inject(ActivatedRoute);
	private readonly router = inject(Router);

	readonly providerId = signal<string | null>(null);

	ngOnInit(): void {
		const providerId = this.route.snapshot.paramMap.get("id");

		if (!providerId) {
			void this.router.navigate(["/app", "providers"]);
			return;
		}

		this.providerId.set(providerId);
		void this.store.loadProviderServices(providerId);
	}

	ngOnDestroy(): void {
		this.store.clearState();
	}

	onBack(): void {
		void this.router.navigate(["/app", "providers"]);
	}

	onRetry(): void {
		const providerId = this.providerId();

		if (!providerId) {
			return;
		}

		void this.store.loadProviderServices(providerId);
	}
}
