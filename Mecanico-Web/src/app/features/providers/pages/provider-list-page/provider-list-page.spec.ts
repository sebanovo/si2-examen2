import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderListPage } from "./provider-list-page";

describe("ProviderListPage", () => {
	let component: ProviderListPage;
	let fixture: ComponentFixture<ProviderListPage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderListPage],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderListPage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
