import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderServiceListPage } from "./provider-service-list-page";

describe("ProviderServiceListPage", () => {
	let component: ProviderServiceListPage;
	let fixture: ComponentFixture<ProviderServiceListPage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderServiceListPage],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderServiceListPage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
